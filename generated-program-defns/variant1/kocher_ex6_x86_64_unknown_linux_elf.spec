prog _generated-binaries_variant1_kocher_ex6_x86_64_unknown_linux_elf {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	and	rax, qword ptr [0x500000];
    4194324:	cmp	rax, qword ptr [rbp - 8];
    4194328:	jne	0x400049;
ENTRY_4194334:
    4194334e:	mov	rax, qword ptr [rbp - 8];
    4194338:	movzx	ecx, byte ptr [rax + 0x500008];
    4194346a:	shl	ecx, 9;
    4194349d:	movsxd	rax, ecx;
    4194352:	movzx	ecx, byte ptr [rax + 0x500010];
    4194360:	movzx	edx, byte ptr [0x500018];
    4194368:	and	edx, ecx;
    4194370:	mov	byte ptr [0x500018], dl;
    4194377:	pop	rbp;
    4194378a:	ret;
ENTRY_4194377:
    4194377:	pop	rbp;
    4194378a:	ret;
}
