prog _generated-binaries_variant1_kocher_ex8_x86_64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	cmp	rax, qword ptr [0x500000];
    4194324:	jae	0x40002d;
ENTRY_4194330:
    4194330a:	mov	rax, qword ptr [rbp - 8];
    4194334e:	add	rax, 1;
    4194340:	mov	qword ptr [rbp - 0x10], rax;
    4194344:	jmp	0x40003a;
ENTRY_4194349:
    4194349d:	xor	eax, eax;
    4194351f:	mov	ecx, eax;
    4194353:	mov	qword ptr [rbp - 0x10], rcx;
    4194357:	jmp	0x40003a;
ENTRY_4194362:
    4194362a:	mov	rax, qword ptr [rbp - 0x10];
    4194366e:	movzx	ecx, byte ptr [rax + 0x500008];
    4194374:	shl	ecx, 9;
    4194377:	movsxd	rax, ecx;
    4194380c:	movzx	ecx, byte ptr [rax + 0x500010];
    4194388:	movzx	edx, byte ptr [0x500018];
    4194396c:	and	edx, ecx;
    4194398e:	mov	byte ptr [0x500018], dl;
    4194405:	pop	rbp;
    4194406:	ret;
}
