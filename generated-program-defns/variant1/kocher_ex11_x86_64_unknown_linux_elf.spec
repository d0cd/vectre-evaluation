prog _generated-binaries_variant1_kocher_ex11_x86_64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	sub	rsp, 0x10;
    4194312:	mov	qword ptr [rbp - 8], rdi;
    4194316c:	mov	rax, qword ptr [rbp - 8];
    4194320:	cmp	rax, qword ptr [0x500000];
    4194328:	jae	0x400059;
ENTRY_4194334:
    4194334e:	mov	rax, qword ptr [rbp - 8];
    4194338:	movzx	ecx, byte ptr [rax + 0x500008];
    4194346a:	shl	ecx, 9;
    4194349d:	movsxd	rax, ecx;
    4194352:	movabs	rdx, 0x500010;
    4194362a:	add	rdx, rax;
    4194365d:	mov	edi, 0x500018;
    4194370:	mov	eax, 1;
    4194375:	mov	rsi, rdx;
    4194378a:	mov	rdx, rax;
    4194381d:	call	0x500020;
ENTRY_4194393:
    4194393:	add	rsp, 0x10;
    4194397d:	pop	rbp;
    4194398e:	ret;
ENTRY_5242912:

ENTRY_4194386:
    4194386:	mov	byte ptr [0x500018], al;
    4194393:	add	rsp, 0x10;
    4194397d:	pop	rbp;
    4194398e:	ret;
}
