prog _generated-binaries_variant1_kocher_ex2_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	byte ptr [rbp - 1], dil;
    4194312:	movzx	eax, byte ptr [rbp - 1];
    4194316c:	shl	eax, 9;
    4194319f:	movsxd	rcx, eax;
    4194322:	movzx	eax, byte ptr [rcx + 0x500000];
    4194330a:	movzx	edx, byte ptr [0x500008];
    4194338:	and	edx, eax;
    4194340:	mov	byte ptr [0x500008], dl;
    4194347b:	pop	rbp;
    4194348c:	ret;
ENTRY_4194352:
    4194352:	push	rbp;
    4194353:	mov	rbp, rsp;
    4194356:	sub	rsp, 0x10;
    4194360:	mov	qword ptr [rbp - 8], rdi;
    4194364c:	mov	rax, qword ptr [rbp - 8];
    4194368:	cmp	rax, qword ptr [0x500010];
    4194376:	jae	0x400061;
ENTRY_4194382:
    4194382e:	mov	rax, qword ptr [rbp - 8];
    4194386:	movzx	edi, byte ptr [rax + 0x500018];
    4194394a:	mov	al, 0;
    4194396c:	call	0x500020;
ENTRY_4194401:
    4194401:	add	rsp, 0x10;
    4194405:	pop	rbp;
    4194406:	ret;
ENTRY_5242912:

ENTRY_4194349:
    4194349d:	nop	dword ptr [rax];
}
